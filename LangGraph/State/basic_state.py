from typing import TypedDict
from langgraph.graph import StateGraph, END

class SimpleState(TypedDict):
    count: int


def increment_state(state: SimpleState) -> SimpleState:
    state['count'] += 1
    return state

def should_continue(state: SimpleState) -> SimpleState:
    if state['count'] < 5:
        return 'continue'
    else:
        return 'stop'
    

graph = StateGraph(SimpleState)

graph.add_node("increment", increment_state)
graph.set_entry_point("increment")
graph.add_conditional_edges(
    'increment',
    should_continue,
    {
        'continue': 'increment',
        'stop': END
    }
)

app = graph.compile()

result = app.invoke({
    'count': 0
})
print(result)