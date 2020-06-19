#!/usr/bin/env python3
# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
from typing import Dict, List, Optional

from pytext.data.sources.data_source import SafeFileWrapper
from pytext.data.sources.tsv import TSV

from ..transforms import Transform
from .base_dataset import BaseDataset


class TsvDataset(BaseDataset):
    def __init__(
        self,
        file_path: str,
        field_names: List[str] = None,
        delimiter: str = "\t",
        batch_size: int = 1,
        is_shuffle: bool = True,
        transforms_dict: Dict[str, List[Transform]] = None,
        batcher=None,
        collate_fn=None,
        chunk_size: int = 1000,
        is_cycle: bool = False,
        limit: Optional[int] = None,
    ):
        field_names = field_names or ["text", "label"]
        self.file = SafeFileWrapper(file_path, encoding="utf-8", errors="replace")
        tsv_iterator = TSV(self.file, field_names=field_names, delimiter=delimiter)
        super().__init__(
            iterable=tsv_iterator,
            batch_size=batch_size,
            is_shuffle=is_shuffle,
            transforms_dict=transforms_dict,
            batcher=batcher,
            collate_fn=collate_fn,
            chunk_size=chunk_size,
            is_cycle=is_cycle,
            limit=limit,
        )
