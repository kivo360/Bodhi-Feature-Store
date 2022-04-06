from typing import Any, Optional, Union
from bodhi_server import FlexModel
from abc import ABC
from bodhi_server.compiler import (
    Token,
    TokenType,
    EdgeTypes,
    UnaryType,
    BinopType,
    NodeType,
)
from bodhi_server.compiler.types import AstType
from bodhi_server import utils


class ASTEdge(FlexModel, ABC):
    type: EdgeTypes


class ASTNode(FlexModel, ABC):
    name: str = utils.hexid()
    value: Optional[Any] = None
    type: AstType = None

    @property
    def has_token(self) -> bool:
        return self.type is not None

    @property
    def is_value(self) -> bool:
        return self.value is not None
