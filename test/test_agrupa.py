from src.agrupador import group, formata, sequence_ends, split_sequences, find_sequences
import unittest


class TestGroup(unittest.TestCase):

    def test_deve_retornar_o_proprio_numero(self):
        self.assertEqual(group([100]), ["[100]"])

    def test_deve_retornar_dois_conjuntos_de_um_numero(self):
        self.assertEqual(group([100, 102]), ["[100]", "[102]"])

    def test_deve_retornar_um_conjunto_com_apenas_uma_sequencia(self):
        self.assertEqual(group([100, 101]), ["[100-101]"])

    def test_deve_retornar_um_conjunto_para_sequencia_de_n_numeros(self):
        self.assertEqual(group(range(100, 150+1)), ["[100-150]"])

    def test_deve_retornar_um_conjunto_para_sequencia_de_n_numeros_e_um_numero(self):
        self.assertEqual(group(list(range(100, 150+1)) +
                               [70]), ["[70]", "[100-150]"])


class TestFormata(unittest.TestCase):

    def test_deve_retornar_grupo_de_um_numero_apenas(self):
        self.assertEqual(formata([100]), "[100]")

    def test_deve_retornar_grupo_de_dois_numeros(self):
        self.assertEqual(formata([100, 101]), "[100-101]")

    def test_deve_retornar_grupo_de_tres_numeros(self):
        self.assertEqual(formata([100, 101, 132]), "[-]")


class TestSequenceEnds(unittest.TestCase):

    def test_deve_retornar_o_primeiro_e_unicao_numero(self):
        self.assertEqual(sequence_ends([100]), [100, 0])

    def test_deve_retornar_o_segundo_da_sequencia(self):
        self.assertEqual(sequence_ends([100, 101]), [101, 1])

    def test_deve_retornar_o_ultimo_da_sequencia_de_n_numeros(self):
        self.assertEqual(sequence_ends(range(100, 105+1)), [105, 5])

    def test_deve_retornar_o_ultimo_da_primeira_sequencia_de_2_sequencias_proximas(self):
        self.assertEqual(sequence_ends(
            list(range(100, 105+1)) + list(range(107, 110+1))), [105, 5])

    def test_deve_retornar_o_ultimo_da_primeira_sequencia_de_2_sequencias_distantes(self):
        self.assertEqual(sequence_ends(
            list(range(100, 105+1)) + list(range(200, 205+1))), [105, 5])


class TestSplitSequences(unittest.TestCase):

    def test_deve_retornar_uma_lista_com_uma_lista_de_sequencia(self):
        self.assertEqual(split_sequences(
            list(range(10, 20+1))), [[10, 20]])

    def test_deve_retornar_uma_lista_com_duas_listas_de_sequencia(self):
        self.assertEqual(
            split_sequences(list(range(10, 20+1)) + list(range(22, 32+1))),
            [[10, 20], [22, 32]])

    def test_deve_retornar_uma_lista_com_uma_lista_de_sequencia_e_um_numero(self):
        self.assertEqual(
            split_sequences(list(range(10, 20+1)) + [22]),
            [[10, 20], [22]])

    def test_deve_retornar_uma_lista_com_duas_listas_de_um_numero(self):
        self.assertEqual(
            split_sequences([20, 22]),
            [[20], [22]])

    def test_deve_retornar_um_conjunto_para_sequencia_de_n_numeros_e_um_numero(self):
        self.assertEqual(split_sequences(list(range(100, 150+1)) +
                                         [170]), [[100, 150], [170]])

    def test_deve_retornar_um_conjunto_para_sequencia_de_n_numeros_e_um_numero(self):
        self.assertEqual(split_sequences(list(range(100, 150+1)) +
                                         [70]), [[100, 150], [70]])


class TestFindSequences(unittest.TestCase):

    def test_deve_retornar_um_conjunto_para_sequencia_de_n_numeros_e_um_numero(self):
        self.assertEqual(find_sequences(list(range(100, 150+1)) +
                                        [170]), [[100, 150], [170]])

    def test_deve_retornar_um_conjunto_para_sequencia_de_n_numeros_e_um_numero_repetido(self):
        self.assertEqual(find_sequences(list(range(100, 150+1)) +
                                        [70]), [[70], [100, 150]])
