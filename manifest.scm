;; Usage: guix shell [-m manifest.scm]

(specifications->manifest '("python"
                            "python-numpy"
                            "python-scipy"
                            "python-matplotlib"
                            "python-pandas"
                            "python-platformdirs"
                            "python-glowgreen"
                            "python-xmltodict"
                            "python-docx"
                            "python-pytest"))
