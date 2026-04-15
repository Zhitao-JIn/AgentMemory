"""添加记忆实现"""
import json
from pathlib import Path
from typing import Any, Dict, List, Optional

_store_path: Optional[str] = None
_memories: List[Dict[str, Any]] = []


def init_memory_storage(path: Optional[str] = None) -> None:
    """初始化存储"""
    global _store_path, _memories
    _store_path = path
    if path and Path(path).exists():
        with open(path, "r", encoding="utf-8") as f:
            _memories = json.load(f)


def add_memory(content: str, meta: Optional[Dict] = None) -> None:
    """添加记忆"""
    global _memories
    _memories.append({"content": content, "meta": meta or {}})
    _save()


def _save() -> None:
    """保存到文件"""
    if _store_path:
        Path(_store_path).parent.mkdir(parents=True, exist_ok=True)
        with open(_store_path, "w", encoding="utf-8") as f:
            json.dump(_memories, f, ensure_ascii=False, indent=2)
