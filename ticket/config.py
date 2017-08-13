from ticket.config_loader import fetch

BRANCH_POINT = fetch('BRANCH_POINT', default='devlopment')
PIVOTAL_PROJECT_ID = fetch('PIVOTAL_PROJECT_ID')
PIVOTAL_API_KEY = fetch('PIVOTAL_API_KEY')
BRANCH_NAME_PREFIX = fetch('BRANCH_NAME_PREFIX', 'PT')
BRANCH_PART_SEPARATOR = fetch('BRANCH_PART_SEPARATOR', '-')
