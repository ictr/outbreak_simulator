import os
import pytest
from covid19_outbreak_simulator.cli import parse_args, main
from covid19_outbreak_simulator.model import Params


def test_plugin_pre_quarantine():
    main([
        '--jobs', '1', '--repeats', '100', '--plugin', 'quarantine',
        '--duration', '7'
    ])
    main([
        '--jobs', '1', '--repeats', '100', '--plugin', 'quarantine', '1', '2',
        '--duration', '7'
    ])
    main([
        '--jobs', '1', '--repeats', '100', '--popsize', 'A=100', 'B=200',
        '--infector', 'A2', 'A7', '--plugin', 'quarantine', 'A2', 'A7',
        '--duration', '7'
    ])


def test_plugin_pre_quarantine_error():
    with pytest.raises(Exception):
        main([
            '--jobs', '1', '--repeats', '100', '--plugin', 'quarantine', '1',
            '2a', '--duration', '7'
        ])


def test_plugin_stat():
    main([
        '--jobs', '1', '--repeats', '100', '--plugin', 'stat', '--interval', '1'
    ])


def test_plugin_sample():
    main([
        '--jobs', '1', '--repeats', '100', '--plugin', 'sample', '--interval',
        '1', '--proportion', '0.8'
    ])
    main([
        '--jobs', '1', '--repeats', '100', '--plugin', 'sample', '--interval',
        '1', '--size', '20'
    ])


def test_plugin_sample_error():
    with pytest.raises(Exception):
        main([
            '--jobs', '1', '--repeats', '100', '--plugin', 'sample',
            '--interval', '1'
        ])

    with pytest.raises(Exception):
        main([
            '--jobs', '1', '--repeats', '100', '--plugin', 'sample',
            '--interval', '1', '--proportion', 'a'
        ])

    with pytest.raises(Exception):
        main([
            '--jobs', '1', '--repeats', '100', '--plugin', 'sample',
            '--interval', '1', '--size', '20', '--proportion', '0.5'
        ])


def test_plugin_dynamic_r0():
    main([
        '--jobs', '1', '--repeats', '100', '--plugin', 'dynamic_r0', '--at',
        '1', '--new-symptomatic-r0', '0.2'
    ])
    main([
        '--jobs', '1', '--repeats', '100', '--plugin', 'dynamic_r0', '--at',
        '1', '--new-asymptomatic-r0', '0.4'
    ])