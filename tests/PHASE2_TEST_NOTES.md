# Phase 2 Validation Notes

## Environment
- OS: Windows
- Python: Virtualenv (activated)
- Execution Mode: python -m simulation.run_simulation

## Simulation Configuration
- Duration: 7 days
- Synthetic User: Burnout-Prone Student
- Seed: 42

## Validation Results
- Simulation completed without errors: YES
- Logs generated for all days: YES (7/7)
- Closed-loop governance verified: YES
- Explainability surfaced for every decision: YES
- Deterministic replay: EXPECTED (fixed seed)

## Observations
- Governance strategies adapted over time (support ↔ stabilization)
- Alarm triggering was conditional and bounded
- User trust showed a net positive change (+0.11)
- Excessive enforcement was avoided

## Conclusion
Phase 2 behavioral simulation for AlarmSM is
functionally complete, deterministic, and validated.


(venv) C:\Manohar\AlarmSM>python -m simulation.run_simulation

================================================================================  
Running AlarmSM Behavioral Simulation (7 days)
================================================================================  

----------------------------------------------------------------------
Day 1
----------------------------------------------------------------------
Strategy           : support
Discipline Level   : 0.50
Failure Risk       : 0.50
Fatigue Index      : 0.50
Avoidance Tendency : 0.30
Momentum Trend     : 0.00
Signals Observed   : ['alarm_failure', 'excessive_snooze', 'late_night_usage']    
Decision Rationale : Trigger='Policy evaluation based on behavioral state' | Strategy=support | Action='Selected support strategy' | Expected='Improved long-term behavioral stability' | Confidence=1.00    
Alarm Triggered    : False
Outcome Success   : False

----------------------------------------------------------------------
Day 2
----------------------------------------------------------------------
Strategy           : stabilization       
Discipline Level   : 0.46
Failure Risk       : 0.60
Fatigue Index      : 0.50
Avoidance Tendency : 0.30
Momentum Trend     : -0.03
Signals Observed   : ['alarm_failure']   
Decision Rationale : Trigger='Policy evaluation based on behavioral state' | Strategy=stabilization | Action='Selected stabilization strategy' | Expected='Improved long-term behavioral stability' | Confidence=1.00
Alarm Triggered    : True
Outcome Success   : True

----------------------------------------------------------------------
Day 3
----------------------------------------------------------------------
Strategy           : stabilization       
Discipline Level   : 0.39
Failure Risk       : 0.85
Fatigue Index      : 0.54
Avoidance Tendency : 0.30
Momentum Trend     : -0.10
Signals Observed   : ['alarm_failure', 'excessive_snooze', 'late_night_usage']    
Decision Rationale : Trigger='Policy evaluation based on behavioral state' | Strategy=stabilization | Action='Selected stabilization strategy' | Expected='Improved long-term behavioral stability' | Confidence=1.00
Alarm Triggered    : True
Outcome Success   : True

----------------------------------------------------------------------
Day 4
----------------------------------------------------------------------
Strategy           : stabilization       
Discipline Level   : 0.46
Failure Risk       : 0.67
Fatigue Index      : 0.54
Avoidance Tendency : 0.30
Momentum Trend     : -0.04
Signals Observed   : ['clean_alarm_dismissal', 'early_wake_success']
Decision Rationale : Trigger='Policy evaluation based on behavioral state' | Strategy=stabilization | Action='Selected stabilization strategy' | Expected='Improved long-term behavioral stability' | Confidence=1.00
Alarm Triggered    : True
Outcome Success   : True

----------------------------------------------------------------------
Day 5
----------------------------------------------------------------------
Strategy           : support
Discipline Level   : 0.50
Failure Risk       : 0.57
Fatigue Index      : 0.54
Avoidance Tendency : 0.30
Momentum Trend     : -0.01
Signals Observed   : ['clean_alarm_dismissal']
Decision Rationale : Trigger='Policy evaluation based on behavioral state' | Strategy=support | Action='Selected support strategy' | Expected='Improved long-term behavioral stability' | Confidence=1.00    
Alarm Triggered    : False
Outcome Success   : False

----------------------------------------------------------------------
Day 6
----------------------------------------------------------------------
Strategy           : stabilization       
Discipline Level   : 0.46
Failure Risk       : 0.75
Fatigue Index      : 0.58
Avoidance Tendency : 0.30
Momentum Trend     : -0.06
Signals Observed   : ['alarm_failure', 'late_night_usage']
Decision Rationale : Trigger='Policy evaluation based on behavioral state' | Strategy=stabilization | Action='Selected stabilization strategy' | Expected='Improved long-term behavioral stability' | Confidence=1.00
Alarm Triggered    : True
Outcome Success   : True

----------------------------------------------------------------------
Day 7
----------------------------------------------------------------------
Strategy           : support
Discipline Level   : 0.40
Failure Risk       : 1.00
Fatigue Index      : 0.62
Avoidance Tendency : 0.30
Momentum Trend     : -0.13
Signals Observed   : ['alarm_failure', 'excessive_snooze', 'late_night_usage']    
Decision Rationale : Trigger='Policy evaluation based on behavioral state' | Strategy=support | Action='Selected support strategy' | Expected='Improved long-term behavioral stability' | Confidence=1.00    
Alarm Triggered    : False
Outcome Success   : False

================================================================================  
Simulation Summary
================================================================================  
Total Days Simulated : 7
Alarms Triggered     : 4
Successful Outcomes : 4
Net Trust Change    : 0.11
================================================================================  

(venv) C:\Manohar\AlarmSM>         