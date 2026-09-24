pipeline {
    agent any

    parameters {
        choice(
            name: 'ENVIRONMENT',
            choices: ['dev', 'staging', 'prod'],
            description: 'Select the deployment environment'
        )
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                bat 'python -m py_compile app.py'
            }
        }

        stage('Deploy') {
            steps {
                input(
                    message: "Approve deployment to ${params.ENVIRONMENT}?",
                    ok: 'Go'
                )

                bat 'python app.py'
            }
        }
    }
}
