#!/bin/bash

( python3 backend/dbserve.py &)
( sudo python3 frontend/app.py &)
