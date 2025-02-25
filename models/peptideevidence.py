from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Text, Integer, BOOLEAN, ForeignKeyConstraint, Index
from models.base import Base


class PeptideEvidence(Base):
    __tablename__ = "peptideevidence"
    upload_id: Mapped[int] = mapped_column(Integer, ForeignKey("upload.id"), index=True, primary_key=True,
                                           nullable=False)
    peptide_id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False, index=True)
    dbsequence_id: Mapped[str] = mapped_column(Text, primary_key=True, nullable=False)
    pep_start: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    is_decoy: Mapped[bool] = mapped_column(BOOLEAN, nullable=True)
    __table_args__ = (
        ForeignKeyConstraint(
            ("dbsequence_id", "upload_id"),
            ("dbsequence.id", "dbsequence.upload_id"),
        ),
        ForeignKeyConstraint(
            ("peptide_id", "upload_id"),
            ("modifiedpeptide.id", "modifiedpeptide.upload_id"),
        ),
        # add index on upload_id, peptide_id
        Index("peptideevidence_upload_id_peptide_id_idx", "upload_id", "peptide_id"),
    )

