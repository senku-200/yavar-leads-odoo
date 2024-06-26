document.addEventListener('DOMContentLoaded',()=>{

    function createPopup(details){
        console.log(JSON.stringify(details))
    }


    function handelClick(event){
        const row = event.target.closest('tr');
        const details = {
            CompanyName:row.children[1].textContent,
            CompanyIndustry:row.children[2].textContent,
            ProjectName:row.children[3].textContent,
            ProjectDescription:row.children[4].textContent,
            FirstName:row.children[5].textContent,
            LastName:row.children[6].textContent,
            Email:row.children[7].textContent,
            PhoneNumber:row.children[8].textContent,
            Country:row.children[9].textContent,
            JobLevel:row.children[10].textContent,
            JobFunction:row.children[11].textContent,
            ProductCloudInterest:row.children[12].textContent,
            IsThisAnRFP:row.children[13].textContent,
            BudgetforProject:row.children[14].textContent,
        };
        createPopup(details);
    }


    document.querySelectorAll('.fa-eye').forEach((button)=>{
        button.addEventListener('click',handelClick)
    })
})