fin = open("data.html", "rt")
    #read file contents to string
data = fin.read()
    #replace all occurrences of the required string
# string='<div class="container mt-5 mb-3"> <div class="row"> <div class="col-md-4"> <div class="card p-3 mb-2"> <div class="d-flex justify-content-between"> <div class="d-flex flex-row align-items-center"> <div class="icon"> <i class="bx bxl-mailchimp"></i> </div> <div class="ms-2 c-details"> <h6 class="mb-0">Vethanathan</h6> <span>4 days ago</span> </div> </div> <div class="badge"> <span>Python</span> </div> </div> <div class="mt-5"> <h3 class="heading">Automatic Attendence System</h3><br> <div class="badge"><button class="btn btn-primary btn-sm"> <i class="fa fa-plus"></i> Download </button> </div> <div class="mt-5"></div> </div> </div> </div> </div> </div> '
data = data.replace("<!-- <p>vetha</p> -->",'<div class="container mt-5 mb-3"> <div class="row"> <div class="col-md-4"> <div class="card p-3 mb-2"> <div class="d-flex justify-content-between"> <div class="d-flex flex-row align-items-center"> <div class="icon"> <i class="bx bxl-mailchimp"></i> </div> <div class="ms-2 c-details"> <h6 class="mb-0">Vethanathan</h6> <span>4 days ago</span> </div> </div> <div class="badge"> <span>Python</span> </div> </div> <div class="mt-5"> <h3 class="heading">Automatic Attendence System</h3><br> <div class="badge"><button class="btn btn-primary btn-sm"> <i class="fa fa-plus"></i> Download </button> </div> <div class="mt-5"></div> </div> </div> </div> </div> </div> <!-- <p>vetha</p> -->')
print(data)
    #close the input file
fin.close()
    #open the input file in write mode
fin = open("data.html", "wt")
    #overrite the input file with the resulting data
fin.write(data)
    #close the file
fin.close()