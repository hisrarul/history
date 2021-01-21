## Blackbox Exporter

https://lyz-code.github.io/blue-book/devops/prometheus/blackbox_exporter/


#### Create prometheus alert rule
```
#https://lapee79.github.io/en/article/monitoring-http-using-blackbox-exporter/
  - name: blackbox-exporter
    rules:
    - alert: ProbeFailed
      expr: probe_success == 0
      for: 5m
      labels:
        severity: error
      annotations:
        summary: "Probe failed (instance {{ $labels.instance }})"
        description: "Probe failed\n  VALUE = {{ $value }}\n  LABELS: {{ $labels }}"
```
