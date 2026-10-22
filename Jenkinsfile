pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Check Python') {
            steps {
                bat '"C:\\Users\\Prapti Patel\\AppData\\Local\\Programs\\Python\\Python310\\python.exe" --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\Prapti Patel\\AppData\\Local\\Programs\\Python\\Python310\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run Automated Tests') {
            steps {
                bat '"C:\\Users\\Prapti Patel\\AppData\\Local\\Programs\\Python\\Python310\\python.exe" -m pytest --junitxml=reports\\test-results.xml'
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true, testResults: 'reports/test-results.xml'
        }
    }
}