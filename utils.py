from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate 
from langchain.chains import LLMChain 
from langchain.tools import DuckDuckGoSearchRun     

#Function to Generate Video Script 

def generate_script(prompt, video_length, creativity, api_key):

    #Template for generating 'Title'
    title_template = PromptTemplate(
        input_variables = ['subject'],
        template = 'Please come up with a title for a YouTube video on the {subject}'
    )

    #Template for generating 'Video Script' using search engine
    script_template = PromptTemplate(
        input_variables = ['title', 'DuckDuckGo_Search', 'duration'],
        template = 'Create a script for a Youtube video based on this title for me. TITLE: {title} of duration: {duration} minutes using this search data {DuckDuckGo_Search}'

    )

    #Setting up OpenAI LLM: 
    llm = ChatOpenAI(temperature = creativity, openai_api_key=api_key, model_name = 'gpt-3.5-turbo')

    #Creating a chain for title and Video Script
    title_chain = LLMChain(llm = llm, prompt=title_template, verbose = True)
    script_chain = LLMChain(llm = llm, prompt=script_template, verbose = True)

    search = DuckDuckGoSearchRun() 

    #Executing the chains we created for "Title"
    title = title_chain.run(prompt)

    #Executing the chains we created for "Video Script" by taking help of search engine "DuckDuckGo"
    search_result = search.run(prompt) #this is to get some data from the search engine 
    script=script_chain.run(title=title, DuckDuckGo_Search = search_result, duration = video_length)

    #return the output 
    return search_result, title, script