# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import json
from atlassian import Jira

# from jira import JIRA

info = json.load(open("login.json"))
username = info['username']
token = info['token']
server = info['server']

from jira import JIRA


class JiraClient:
    def __init__(self, server, username, token):
        self.jira = JIRA(server, basic_auth=(username, token))

    def get_issue(self, issue_key):
        issue = self.jira.issue(issue_key)
        return issue

    def create_issue(self, project_key, summary, description, issue_type):
        new_issue = self.jira.create_issue(project=project_key, summary=summary,
                                           description=description, issuetype={'name': issue_type})
#         return new_issue
    def get_current_user(self):
        return self.jira.current_user()

    def get_project(self, project_key):
        return self.jira.project(project_key)
    #
    def get_issues(self, jql):
        return self.jira.search_issues(jql)


def main():
    ## Instantiating method 2
    jira = JiraClient(server, username, token)

    print('++++++++++++++++++jira object++++++++++++')
    print(jira)

    print('++++++++++++++++++jira one issue++++++++++++')
    # issue = jira.get_issue('SSP')
    # print(issue)

    print('++++++++++jira issue about to be created+++++')
    # new_issue = jira.create_issue(project_key='SSP',
    #                             summary='New Issue',
    #                             description='This is a new issue',
    #                             issue_type='Task')
    # print(new_issue)

    print('++++++++++++++++++jira current user++++++++++++')
    current_user = jira.get_current_user()
    #
    print('++++++++++++++++++jira project++++++++++++')
    # project = jira.get_project("SSP-2")
    # print(project)
    #
    print('++++++++++++++++++jira issues++++++++++++')
    # print('issues')
    # issues = jira.get_issues("project = DESK")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
