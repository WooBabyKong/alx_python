import importlib.machinery

if __name__ == "__main__":
    loader = importlib.machinery.SourceFileLoader('variable_load_2', 'variable_load_2.py')
    module = loader.load_module()
    
    a = module.a
    print(a)