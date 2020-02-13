####this file is only used for continuous evaluation test!

import os
import sys
sys.path.insert(0, os.environ['ceroot'])
from kpi import CostKpi, DurationKpi, AccKpi

#### NOTE kpi.py should shared in models in some way!!!!


train_duration_sts_b_card1 = DurationKpi(
    'train_duration_sts_b_card1', 0.01, 0, actived=True)
train_cost_sts_b_card1 = CostKpi(
    'train_cost_sts_b_card1', 0.02, 0, actived=True)
train_duration_sts_b_card4 = DurationKpi(
    'train_duration_sts_b_card4', 0.04, 0, actived=True)
train_cost_sts_b_card4 = CostKpi(
    'train_cost_sts_b_card4', 0.08, 0, actived=True)

tracking_kpis = [
    train_duration_sts_b_card1,
    train_cost_sts_b_card1,
    train_duration_sts_b_card4,
    train_cost_sts_b_card4,
]


def parse_log(log):
    '''
    This method should be implemented by model developers.
    The suggestion:
    each line in the log should be key, value, for example:
    "
    train_cost\t1.0
    test_cost\t1.0
    train_cost\t1.0
    train_cost\t1.0
    train_acc\t1.2
    "
    '''
    for line in log.split('\n'):
        fs = line.strip().split('\t')
        print(fs)
        if len(fs) == 3 and fs[0] == 'kpis':
            print("-----%s" % fs)
            kpi_name = fs[1]
            kpi_value = float(fs[2])
            yield kpi_name, kpi_value


def log_to_ce(log):
    kpi_tracker = {}
    for kpi in tracking_kpis:
        kpi_tracker[kpi.name] = kpi

    for (kpi_name, kpi_value) in parse_log(log):
        print(kpi_name, kpi_value)
        kpi_tracker[kpi_name].add_record(kpi_value)
        kpi_tracker[kpi_name].persist()


if __name__ == '__main__':
    log = sys.stdin.read()
    print("*****")
    print(log)
    print("****")
    log_to_ce(log)
