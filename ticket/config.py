from ticket.config_loader import fetch

BRANCH_POINT = fetch('BRANCH_POINT', default='development')
PIVOTAL_PROJECT_ID = fetch('PIVOTAL_PROJECT_ID')
PIVOTAL_API_KEY = fetch('PIVOTAL_API_KEY')
GITHUB_API_KEY = fetch('GITHUB_API_KEY')
GITHUB_REPO_OWNER = fetch('GITHUB_REPO_OWNER')
BRANCH_ID_PREFIX = fetch('BRANCH_ID_PREFIX', 'PT')
BRANCH_PART_SEPARATOR = fetch('BRANCH_PART_SEPARATOR', '-')
