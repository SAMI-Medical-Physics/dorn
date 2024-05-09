;; Usage: guix shell [-m manifest.scm]

(specifications->manifest '("python"
                            "python-numpy"
                            "python-scipy"
                            "python-matplotlib"
                            "python-pandas"
                            "python-glowgreen"
                            "python-xmltodict"
                            "python-docx"
                            "python-pytest"))
