from enum import Enum
class Strategy(Enum):
    """
    High-level governance strategies
    selectable by the Governing Brain.
    """

    ENFORCEMENT = "enforcement"
    COMPENSATION = "compensation"
    STABILIZATION = "stabilization"
    SUPPORT = "support"
    STRATEGIC_PAUSE = "strategic_pause"
