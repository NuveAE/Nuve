"""Current Nuve pricing for the follow-up page's pricing section (--pricing).
Change prices here once, never per prospect."""

PLAN_NAME = 'Always On E'
PLAN_MONTHLY = 1487          # all features, flat monthly

# (feature, what it does, a la carte monthly price)
FEATURES = [
    ('Unlimited custom app', 'Your own branded app for every customer', 389),
    ('Unlimited logo hosting', 'Your logo on every thermostat screen', 389),
    ('Messaging', 'Maintenance reminders and promos right on the thermostat', 289),
    ('Performance test', 'Virtual performance testing, no truck roll', 289),
    ('Dashboard access', 'Every install, alert and request in one place', 189),
    ('AI reporting', 'System reports that surface repair and replacement work', 189),
    ('Alerts', 'Real-time system alerts to you and the homeowner', 189),
    ('Sensor monitoring', 'Water leak and air/humidity sensors watched 24/7', 189),
]

# (name, model line, price per unit, detail, badge, image in assets/)
HARDWARE = [
    ('V1', 'Sofia V1', 179, 'Branded with your logo and contact info', '', 'stat-v1.png'),
    ('V2', 'Sofia AI V2', 279, 'Comes with 2 sensors: water leak + air/humidity', 'Most popular', 'stat-v2.png'),
    ('V3', 'Sofia Pro V3', 99, 'Pre-order now, ships Q1 2027', 'Pre-order', 'stat-v3.png'),
]
