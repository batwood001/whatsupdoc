# whatsupdoc
A dead-simple healthcheck service

## how to use

1. Clone this repo
2. Configure `config.json`:
    - `startup_delay`: seconds to wait before first heartbeat
    - `interval`: seconds between heartbeats
    - `endpoint`: healthcheck url
    - `failures`: number of consecutive failed healthchecks before alerting
    - `timeout`: request timeout on healthcheck url
3. `python index.py config.json`

## todos

- Enable responses to notifications to reset healthcheck
- Add support for sms + email notifications
