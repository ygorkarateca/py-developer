linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)