# ticket

A command line tool to simplify using Pivotal Tracker and GitHub.

## Installation

This assumes that you have `python3` installed.

1. Clone this repo into a location you want to keep your installation.
2. Run `make install`

## Usage

### `ticket start <pivotal_ticket_id>`

* Starts the ticket on Pivotal
* Creates a new branch in the current repo, generating the branch name from the ticket's title

### `ticket create_pull`

* Creates a pull request for the current branch
* Adds the URL of the pull request to the current ticket (inferred from current branch name)
* Adds the URL of the current ticket to the pull request

## Config

Config variables can be set in `~/.ticket.json` or as environment variables with `TICKET_` added as a prefix.

### Required config variables

* `PIVOTAL_API_KEY` - Your API token for Pivotal
* `PIVOTAL_PROJECT_ID` - The id of the Pivotal project to interface with
* `GITHUB_REPO_OWNER` - The user / organisation on GitHub that owns the current repo
* `GITHUB_API_KEY` - Your GitHub API token. It needs to have the repo and user permissions: https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/
