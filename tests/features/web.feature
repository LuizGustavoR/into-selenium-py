@web
Feature: DuckDuckGo Web Browsing
    As a web surfer,
    I want to find information online,
    So I can learn new things and get tasks done.
 
    Background:
        Given the DuckDuckGo home page is displayed
   
    @basic-search
    Scenario: Basic DuckDuckGo Result Title
        When the user searches for "123"
        Then results title contains "123"
 
    @scenario-outline
    Scenario Outline: Basic DuckDuckGo Search
        When the user searches for <name>
        Then results are shown for <found_animal>
 
    Examples: Animals
        | name       | found_animal |
        | panda      | panda        |
        | python     | python       |
        | polar bear | polar bear   |
 
    @basic-search @independence-search
    Scenario: Lengthy DuckDuckGo Search
        When the user searches for the phrase:
            """
            When in the Course of human events, it becomes necessary for one people
            to dissolve the political bands which have connected them with another,
            and to assume among the powers of the earth, the separate and equal
            station to which the Laws of Nature and of Nature's God entitle them,
            a decent respect to the opinions of mankind requires that they should
            declare the causes which impel them to the separation.
            """
        Then one of the results contains "Declaration of Independence"
