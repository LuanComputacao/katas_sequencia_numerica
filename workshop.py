import io
import sys
from src.agrupador import group

if __name__ == "__main__":
    '''
    use o seguinte comando para executar
    
    python -m unittest test_workshop.py
    '''
    print(group([100, 101, 102, 103, 104, 105, 110, 111, 113, 114, 115, 150, 70]))
