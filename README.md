# AlarmSM – Governing Brain v1.0

AlarmSM is a deterministic behavioral governance engine designed to decide
*how discipline should be applied* (support, stabilization, enforcement)
based on behavioral state, fatigue, momentum, and situational importance.

## What this is
- A policy-driven decision engine
- Context-aware and burnout-safe
- Deterministic and explainable
- Architecture-first design

## What this is NOT
- Not an alarm app
- Not an ML model
- Not an Android implementation

## Core Concepts
- Behavioral state evolution
- Explicit governance policies
- Context-aware enforcement
- Separation of governance and execution

## Project Status
✅ Governing Brain v1.0 is complete, validated, and frozen.  
Future work may include execution adapters or ML advisory layers
without modifying the core logic.

## License
MIT (or Academic Use Only)


AlarmSM
|_______governing_brain
|            |______policies
|            |              _____ __init__.py
|            |           |_____ burnout.py
|            |           |_____context.py
|            |           |______enforcement.py
|            |           |______router.py
|            |           |_______support.py
|            |______ __init__.py
|            |______ explanations.py
|            |______ inputs.py
|            |______ outputs.py
|            |______ state_model.py
|            |_______ strategies.py
|_______venv
|_______context_test.py
|_______README.md
|________test_brain.py