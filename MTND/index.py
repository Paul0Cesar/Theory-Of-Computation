

class Graph(object):

    def __init__(self, vertices):
        self.vertices = {}
        for vertice in vertices:
            self.vertices[vertice] = {}

    def get_vertices(self):
        '''get all vertices'''
        return list(self.vertices.keys())

    def print_edges(self):
        '''print all edges'''
        for key in self.vertices.keys():
            for edge in self.vertices[key]:
                print(key, edge)

    def set_edges(self, edges):
        '''add group of new edges'''
        for origin, char_read, destiny, write, tape_direction in edges:
            self.add_edge(origin, char_read, destiny, write, tape_direction)

    def add_edge(self, origin, char_read, destiny, write, tape_direction):
        '''add new edges to the graph  <Origem,char lido,destino,escreve,direção da fita(I,E,D)>'''
        if str(char_read) not in self.vertices[str(origin)]:
            self.vertices[str(origin)][str(char_read)] = {}

        if str(destiny) not in self.vertices[str(origin)][str(char_read)]:
            self.vertices[str(origin)][str(char_read)][str(destiny)] = {}

        self.vertices[str(origin)][str(char_read)][str(
            destiny)] = (write, tape_direction)

    def get_destiny_vertices_with(self, origin, char_read):
        '''get all vertice destinations'''
        try:
            result = self.vertices.get(str(origin)).get(str(char_read))
            return result if result is not None else {}
        except KeyError:
            return {}

    def __len__(self):
        return len(self.vertices)

    def __str__(self):
        return f'{self.__class__.__name__}({dict(self.vertices)})'

    def __getitem__(self, v):
        return self.vertices[v]


def change_tape_index(index, direction):
    '''move the tape using the args'''
    if str(direction) == "D":
        index = index+1
    elif str(direction) == "E":
        index = index-1
    return index


def update_tape(tape, index, write_char):
    '''update the tape using the args'''
    if len(tape)-1 < index:
        tape.append("*")
    tape[index] = write_char


def process(mtnd, new_state, write_char, tape_direction, tape_index, tape, processing_stack, end_state_set):
    '''function responsible for processing new transition'''
    update_tape(tape, tape_index, write_char)
    tape_index = change_tape_index(tape_index, tape_direction)
    actual_char = "*" if len(tape)-1 < tape_index else tape[tape_index]
    vertices = mtnd.get_destiny_vertices_with(new_state, actual_char)
    if new_state in end_state_set:
        if len(vertices) == 0:
            return 'S'
    processing_stack.append((new_state, tape, tape_index))
    return 'N'


def verify_word(mtnd, word, start_state, end_state_set, tape_left_limit, blank_symbol):
    '''Analyze the word using the MTND passed'''
    first_tape = [tape_left_limit]
    first_tape.extend(list(word.strip()))
    first_tape.append(blank_symbol)

    processing_stack = [(start_state, first_tape, 1)]
    while processing_stack:
        actual_process = processing_stack.pop()
        actual_state = actual_process[0]
        tape = actual_process[1]
        tape_index = int(actual_process[2])
        actual_char = "*" if len(tape)-1 < tape_index else tape[tape_index]

        vertices = mtnd.get_destiny_vertices_with(actual_state, actual_char)
        for new_state in vertices.keys():
            write_char, tape_direction = vertices.get(new_state)
            tmp_tape = tape.copy()
            result = process(mtnd, new_state, write_char, tape_direction, tape_index,
                             tmp_tape, processing_stack, end_state_set)
            if result == "S":
                return "S"
    return "N"


def start(states, alphabet, tape_alphabet, tape_left_limit, blank_symbol, edges, start_state, end_state_list, words):
    '''start the analysis process using the passed args'''
    graph = Graph(states)
    graph.set_edges(edges)
    result = []
    for word in words:
        result.append(verify_word(graph, word, start_state, set(
            end_state_list), tape_left_limit, blank_symbol))
    return result


if __name__ == "__main__":
    states = input().split(" ")
    alphabet = input().split(" ")
    tape_alphabet = input().split(" ")
    tape_left_limit = input()
    blank_symbol = input()

    states_number = int(input())
    edges = []
    for i in range(states_number):
        edge = input().split(" ")
        edges.append((edge[0], edge[1], edge[2], edge[3], edge[4]))
    start_state = input()
    end_state_list = input().split(" ")
    words = input().split(" ")

    for payload in start(states, alphabet, tape_alphabet, tape_left_limit, blank_symbol, edges, str(start_state), end_state_list, words):
        print(payload)
