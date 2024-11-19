pipeline {
    agent any

    environment {
        // Variables de entorno necesarias para el pipeline
        DOCKER_COMPOSE_FILE = 'docker-compose.yml'
        APP_NAME = 'docker-u'
    }

    stages {
        stage('Clonar Repositorio del proyecto') {
            steps {
                // Clonar el repositorio desde Git
                git 'https://tu-repositorio-git.git'
            }
        }

        stage('Construir Imagen Docker para el proyecto') {
            steps {
                // Construir las imágenes Docker usando Docker Compose
                script {
                    sh 'docker-compose -f ${DOCKER_COMPOSE_FILE} build'
                }
            }
        }

        stage('Levantar Contenedores') {
            steps {
                // Levantar los contenedores Docker
                script {
                    sh 'docker-compose -f ${DOCKER_COMPOSE_FILE} up -d'
                }
            }
        }

        stage('Pruebas (no tenemos)') {
            steps {
                // Ejecutar pruebas dentro del contenedor
                // Reemplaza `nombre_de_tu_contenedor` con el nombre del contenedor web
                script {
                    sh 'docker-compose exec web python manage.py test'
                }
            }
        }

        stage('Despliegue del proyecto a produccion') {
            steps {
                // Si todo está bien, puedes realizar un despliegue
                echo 'Despliegue completado exitosamente'
            }
        }
    }

    post {
        always {
            // Limpieza después de que el pipeline se ejecute, éxito o fallo
            echo 'Limpiando contenedores e imágenes temporales'
            sh 'docker-compose -f ${DOCKER_COMPOSE_FILE} down'
        }
    }
}
