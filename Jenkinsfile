pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker{
                   image 'python:3.8-alpine'
                }
              }
           
       steps {
                sh 'python -m py_compile cal_code.py'
           stash(name: 'compiled-results', includes: '*.py*')

            }
           
        }
       
        stage('Test') {
            agent {
                docker {
                    image 'qnib/pytest:latest'
                }
            }
            steps {
                sh 'py.test --junit-xml test-reports/results.xml cal_test.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }

        
       
    }
}
