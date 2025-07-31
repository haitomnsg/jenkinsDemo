pipeline {
    agent any

    environment {
        VENV_DIR = 'C:/Users/haito/.conda/envs/machine_learning'
    }

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/haitomnsg/jenkinsDemo'
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh 'C:/Users/haito/.conda/envs/machine_learning/Scripts/pytest'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    pkill -f app.py || true
                    nohup C:/Users/haito/.conda/envs/machine_learning/Scripts/python app.py > log.txt 2>&1 &
                '''
            }
        }
    }
}