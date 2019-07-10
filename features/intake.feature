Feature: Add Client
    As a logged-in Drug Court user
    I want to be able to add new Clients

    Scenario: Create a Client

        Given I am a logged-in user with the correct permissions

        When I create a client with "Jane"
            And I add a Referral
            And I add a Note

        Then I will be redirected to the Client Detail View