pipeline {
    agent any

    environment {
        PYTHON_PATH = 'C:/Users/haito/.conda/envs/machine_learning/python.exe'
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
                    "%PYTHON_PATH%" -m pytest test_app.py
                """
            }
        }

        stage('Deploy') {
            steps {
                bat '''
                    :: Kill running app if PID file exists
                    if exist app.pid (
                        for /f %%p in (app.pid) do taskkill /F /PID %%p
                        del app.pid
                    ) else (
                        echo No PID file found, starting fresh.
                    )

                    :: Start the Flask app from current workspace
                    start /B "" "%PYTHON_PATH%" "%WORKSPACE%\\app.py"

                    :: Sleep 1s (ping workaround for Jenkins)
                    ping -n 2 127.0.0.1 > NUL

                    :: Save the new PID (simplistic approach)
                    for /f "tokens=2" %%a in ('tasklist /fi "imagename eq python.exe" /fo table ^| findstr /i "python.exe"') do (
                        echo %%a > app.pid
                    )
                '''
            }
        }
    }
}