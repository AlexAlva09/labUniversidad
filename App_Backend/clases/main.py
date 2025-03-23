from universidad import Universidad
from profesor import Profesor
from curso import Curso
from estudiante import Estudiante


def main():
    # Crear universidad
    universidad = Universidad("Universidad de El Salvador")
    
    # Crear profesores
    prof_matematicas = Profesor("Juan Perez", 30, "M", "PROF001", "Matemáticas")
    prof_fisica = Profesor("Maria Lopez", 35, "F", "PROF002", "Física")
    prof_quimica = Profesor("Pedro Ramirez", 40, "M", "PROF003", "Química")
    
    # Crear cursos
    curso_matematicas = Curso("Matemáticas", "MAT101", prof_matematicas)
    curso_fisica = Curso("Física", "FIS101", prof_fisica)
    curso_quimica = Curso("Química", "QUI101", prof_quimica)
    
    # Agregar cursos a la universidad
    universidad.agregar_curso(curso_matematicas)
    universidad.agregar_curso(curso_fisica)
    universidad.agregar_curso(curso_quimica)
    
    # Crear estudiante
    estudiante = Estudiante("Carlos Perez", 20, "M", "202010101", "Ingeniería en Sistemas Informáticos")
    
    # Imprimir detalles
    print("\n=== Detalles de la Universidad ===")
    print(universidad)
    
    print("\n=== Detalles del Estudiante ===")
    print(estudiante)
    
    print("\n=== Detalles de un Profesor ===")
    print(prof_matematicas)
    
    print("\n=== Detalles de un Curso ===")
    print(curso_matematicas)
    
    # Crear y agregar nuevo curso de física
    nuevo_curso_fisica = Curso("Física", "FIS101", prof_fisica)
    universidad.agregar_curso(nuevo_curso_fisica)
    
    print("\n=== Detalles actualizados de la Universidad ===")
    print(universidad)

if __name__ == "__main__":
    main()