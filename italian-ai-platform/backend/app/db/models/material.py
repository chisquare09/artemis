from typing import List, Optional

from sqlalchemy import ForeignKey, Index, Integer, JSON, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base, TimestampMixin, generate_uuid


class Material(Base, TimestampMixin):
    __tablename__ = "materials"
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=generate_uuid)
    title: Mapped[str] = mapped_column(String(255))
    description: Mapped[Optional[str]] = mapped_column(Text)
    source_type: Mapped[Optional[str]] = mapped_column(String(50))
    source_url: Mapped[Optional[str]] = mapped_column(Text)
    language: Mapped[str] = mapped_column(String(10))
    raw_text: Mapped[Optional[str]] = mapped_column(Text)
    chunks: Mapped[List["MaterialChunk"]] = relationship(back_populates="material")
    sources: Mapped[List["MaterialSource"]] = relationship(back_populates="material")


class MaterialSource(Base, TimestampMixin):
    __tablename__ = "material_sources"
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=generate_uuid)
    material_id: Mapped[str] = mapped_column(ForeignKey("materials.id"))
    provider: Mapped[str] = mapped_column(String(50))
    external_id: Mapped[Optional[str]] = mapped_column(String(255))
    metadata_json: Mapped[Optional[dict]] = mapped_column(JSON)
    material: Mapped["Material"] = relationship(back_populates="sources")


class MaterialChunk(Base, TimestampMixin):
    __tablename__ = "material_chunks"
    __table_args__ = (Index("ix_material_chunks_material_id", "material_id"),)
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=generate_uuid)
    material_id: Mapped[str] = mapped_column(ForeignKey("materials.id"))
    chunk_index: Mapped[int] = mapped_column(Integer)
    content: Mapped[str] = mapped_column(Text)
    token_count: Mapped[Optional[int]] = mapped_column(Integer)
    metadata_json: Mapped[Optional[dict]] = mapped_column(JSON)
    material: Mapped["Material"] = relationship(back_populates="chunks")


class UnitMaterialLink(Base, TimestampMixin):
    __tablename__ = "unit_material_links"
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=generate_uuid)
    unit_id: Mapped[str] = mapped_column(ForeignKey("units.id"))
    material_id: Mapped[str] = mapped_column(ForeignKey("materials.id"))
    purpose: Mapped[Optional[str]] = mapped_column(String(100))
