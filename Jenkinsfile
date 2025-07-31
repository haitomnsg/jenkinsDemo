pipeline {
    agent any

    environment {
        PYTHON_PATH = 'C:\\Users\\haito\\anaconda3\\envs\\machine_learning\\python.exe'
    }

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/haitomnsg/jenkinsDemo'
            }
        }

        stage('Run Unit Tests') {
            steps {
                bat """
                    "%PYTHON_PATH%" -m pytest
                """
            }
        }

        stage('Deploy') {
            steps {
                bat """
                    taskkill /F /IM python.exe || echo "No running app"
                    start /B "" "%PYTHON_PATH%" app.py
                """
            }
        }
    }
}
