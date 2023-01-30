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


# +++++++++++++++++++++
# METHOD 1
# +++++++++++++++++++++

class AtlasClient:
    def __int__(self):
        self.client = Jira(server, username, token, cloud=True)

    def project_getter(self, project, issuetype):
        # self.attribute = "This is an attribute"
        jql_request = f'{project} AND issuetype = {issuetype}'  # '"epic link" = WSP-144'
        issues = self.client.jql(jql_request)
        print('PRINTING METHOD 1 QUERY')
        print(issues)
        print(jql_request)


    # def method_2(self):
    #     self.method_1()
    #     print("Accessing attribute:", self.attribute)

# obj = MyClass()
# obj.method_2()



# def jira_client(self, server, username, token):
#     client = Jira(server, username, token, cloud=True)
#     print('printing JIRA')
#     print(client)
#     # jql_request = f'project = SSP AND issuetype = Story'  # '"epic link" = WSP-144'
#     # issues = self.jira.jql(jql_request)
#     # print('PRINTING METHOD 1 QUERY')
#     # print(issues)
#     # print(jql_request)
#
#
# def get_project(self, project, issuetype):
#     jira_client(server, username, token, True)
#     jql_request = f'project = {project} AND issuetype = {issuetype}'  # '"epic link" = WSP-144'
#     issues = self.jira.jql(jql_request)
#     print('PRINTING METHOD 1 QUERY')
#     print(issues)
#     #     print(jql_request)


# +++++++++++++++++++++
# METHOD 2
# +++++++++++++++++++++
from jira import JIRA


# class JiraClient:
#     def __init__(self, server, username, token):
#         self.jira = JIRA(server, basic_auth=(username, token))
#
#     def get_issue(self, issue_key):
#         issue = self.jira.issue(issue_key)
#         return issue
#
#     def create_issue(self, project_key, summary, description, issue_type):
#         new_issue = self.jira.create_issue(project=project_key, summary=summary,
#                                            description=description, issuetype={'name': issue_type})
#         return new_issue


#
#
# # Usage example


def main():
    # ## Instantiating method 1
    jir = AtlasClient()
    # jir.get_project('SSP', 'Story')

    ## Instantiating method 2
    # jira = JiraClient(server, username, token)
    #
    # print('++++++++++++++++++jira++++++++++++')
    # print(jira)
    # issue = jira.get_issue('SSP-1')
    # print(issue)
    # new_issue = jira.create_issue(project_key='SSP', summary='New Issue', description='This is a new issue',
    #                               issue_type='Task')
    # print(new_issue)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
