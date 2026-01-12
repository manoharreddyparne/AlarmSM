from typing import List, Optional

from governing_brain.brain import GoverningBrain
from governing_brain.state_model import BehavioralState, update_state
from governing_brain.inputs import SignalBatch

from simulation.synthetic_users import SyntheticUser
from simulation.metrics import SimulationLog


class TimeEngine:
    """
    Advances time in discrete steps (days) and
    orchestrates governance decision cycles.
    """

    def __init__(
        self,
        brain: GoverningBrain,
        user: SyntheticUser,
        total_days: int = 30,
    ):
        self.brain = brain
        self.user = user
        self.total_days = total_days

        self.current_day: int = 0
        self.state: Optional[BehavioralState] = None
        self.logs: List[SimulationLog] = []

    def run(self) -> List[SimulationLog]:
        for day in range(1, self.total_days + 1):
            self.current_day = day
            self._run_single_day()
        return self.logs

    def _run_single_day(self):
        # 1. Generate signals
        signal_batch: SignalBatch = self.user.generate_signals(
            day=self.current_day,
            state=self.state,
        )

        # 2. Update behavioral state
        self.state = update_state(self.state, signal_batch)

        # 3. Governance decision
        directive, explanation = self.brain.decide(self.state)

        # 4. User reaction (ground truth)
        reaction = self.user.react(directive)

        # 5. Log full cycle
        self.logs.append(
            SimulationLog(
                day=self.current_day,
                state=self.state,
                signals=signal_batch,
                directive=directive,
                explanation=explanation,
                alarm_triggered=reaction.alarm_triggered,
                outcome_success=reaction.outcome_success,
                trust_delta=reaction.trust_delta,
            )
        )
