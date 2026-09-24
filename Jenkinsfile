pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                bat 'python -m py_compile app.py'
                sleep time: 20, unit: 'SECONDS'
                milestone 1
            }
        }

        stage('Deploy') {
            steps {
                milestone 2
                echo 'Deploying application'
            }
        }
    }
}
