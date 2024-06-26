document.addEventListener('DOMContentLoaded',()=>{

  const products = [
      {
        logo: "product_yavar/static/src/assets/zypher.png",
        title: "Zyper",
        description:
          "Streamlines document handling, condensing lengthy content into concise summaries. Perfect for professionals and students, it ensures quick comprehension, time efficiency, and most importantly, data privacy.",
        link: "https://zyphernew.yavar.ai",
        category:'genai',
        username:'demoUser',
        password:'demouser@123'
      },
      {
        logo: "product_yavar/static/src/assets/zypher_chrome.png",
        title: "Zypher  2.0",
        description:
          "Summarize Buttons in Outlook, Gmail, and YouTube: Receive summarized mail in Gmail and Outlook, and enjoy condensed content in YouTube's side panel for English videos under 15 minutes.",
        link: "https://chromewebstore.google.com/detail/zypher/jnffiijebiflabpekpfphicmifknpgep",
        category:'genai',
        username:'',
        password:'',
      },
      {
        logo: "product_yavar/static/src/assets/Ellipse 1.png",
        title: "Gloq",
        description:
          "Glopq is a smart travel companion created to make trip planning easier and more enjoyable. It uses advanced technology to understand your needs and preferences, providing personalized suggestions and assistance every step of the way.",
        link: "https://virtualmind.yavar.ai/",
        category:'genai',
        username:'',
        password:'',
      },
      {
        logo: "product_yavar/static/src/assets/ai_translator.png",
        title: "Translation AI",
        description:
          "Our company has developed a state-of-the-art translation AI. This AI leverages advanced algorithms and neural networks to accurately translate text and speech between multiple languages.",
        link: "https://translate.yavar.ai/login",
        category:'',
        username:'',
        password:'',
      },
      {
        logo: "product_yavar/static/src/assets/Ellipse 1.png",
        title: " Interview Chatbot ",
        description:
          "INTERVIEW-BOT is an advanced AI-driven interview solution that uses Speech Recognition for seamless candidate interactions. It offers dynamic job position interviews, allowing candidates to choose their desired position from a dropdown menu.",
        link: " https://interviewbot.yavar.ai/",
        category:'genai',
        username:'',
        password:'',
      },
      {
        logo: "product_yavar/static/src/assets/xlogo.png",
        title: "Facefusion ",
        description:
          "FaceFusion is a free-to-use web application accessible via the URL facefusion.yavar.ai This innovative tool seamlessly blends users' facial features with various ethnicities and attires from around the world.",
        link: "https://facefusion.yavar.ai/",
        category:'cv',
        username:'',
        password:'',
      },
      {
        logo: "product_yavar/static/src/assets/copper.svg",
        title: "CX",
        description:
          "Give support your customers will rave about. Your customers want to connect any time, any place. Copper makes it easy to support your customers across all of your channels – from email to WhatsApp to Phone Calls and more. Powered by AI.",
        link: "https://hellocopper.ai/",
        category:'',
        username:'',
        password:'',
      },
      {
        logo: "product_yavar/static/src/assets/blr_airport.svg",
        title: "Screener",
        description:
          "Enjoy lightning-fast internet speeds while waiting for your flight. Stay connected with friends, family, and work hassle-free.Say goodbye to data limits and roaming charges. With our complimentary Wi-Fi, your travel experience becomes smoother and more enjoyable.",
        link: "https://scanner.yavar.ai/",
        category:'',
        username:'',
        password:'',
      },
      {
        logo: "product_yavar/static/src/assets/Ellipse 1.png",
        title: "Call-In",
        description:
          "Transform Your Customer Experience with CALL-IN!Eliminate long wait times and frustrating menus. CALL-IN leverages AI and NLP for:Speedy Responses & ScalabilityCustomization & Top-Tier Customer Experiences CALL-IN.",
        link: "static_page_call-in.html",
        category:'genai',
        username:'',
        password:'',
      },
      {
        logo: "product_yavar/static/src/assets/Ellipse 1.png",
        title: "VisionIQ ",
        description:
          "Unleash the potential of your space with cutting-edge computer vision technology. Our solutions go beyond image capture, enhancing safety, efficiency, and customer experience. From real-time parking updates to instant fall detection, we empower you to see further and do more.",
        link: "staic_page_VisionIQ.html",
        category:'cv',
        username:'',
        password:'',
      },
    ];

    const createElementFunction = (elementType,elementclassName)=>{
      const newElement = document.createElement(`${elementType}`);
      newElement.className = elementclassName;
      return newElement;
    }
    const appendElement = (appender,appended)=>{
      appender.appendChild(appended);
    }
    function createAndAppend(elementType,elementclassName,appender) {
      const newCreatedElement = createElementFunction(elementType,elementclassName);
      appendElement(appender,newCreatedElement);
      return newCreatedElement
    }
    const header_generator = (element,title)=>{
      const container = document.createElement('div');
      const container_title = document.createElement('p');
      const icon_container = document.createElement('div');

      container.className = 'collapseExtendContainer';
      container_title.innerHTML = `${title}`; 
      icon_container.innerHTML = '<i class="fa-solid fa-angle-up"></i>';

      container.appendChild(container_title);
      container.appendChild(icon_container);

      element.appendChild(container);
    }
    

    const productContainer = document.getElementById("product-container");

    const genai_group  = createAndAppend('section','genai_grp',productContainer);
    const cv_group  = createAndAppend('section','cv_grp',productContainer);
    const others_grp  = createAndAppend('section','others_grp',productContainer);

    header_generator(genai_group,'genai');
    header_generator(cv_group,'computer vision');
    header_generator(others_grp,'others');
    
    let productsAppendingList = {};


    products.forEach((product,index) => {
      const productSection = document.createElement("section");
      productSection.className = "product_con";

      productSection.innerHTML = `
        <article class="product_logo_con">
          <div class="product_logo">
            <img src="${product.logo}" alt="${product.title} Logo" />
          </div>
          <div class="product_title">
            <p>${product.title}</p>
          </div>
        </article>
        <article class="content_con">
          <p>${product.description}</p>
          <a class="redirect-btn" index='${index}'>
            Click Here<i class="fa-solid fa-arrow-right"></i>
          </a>
          <i style='visibility:hidden;value:${index}'></i>
        </article>
          `;
      // <a href="${product.link}" target="_blank" class="redirect-btn">
      switch(product.category){
        case 'genai':
          if ('genai' in productsAppendingList){
            productsAppendingList.genai.push(productSection);
          }
          else{
            productsAppendingList.genai = [productSection]
          }
          break;
        case 'cv':
          if ('cv' in productsAppendingList){
            productsAppendingList.cv.push(productSection);
          }
          else{
            productsAppendingList.cv = [productSection]
          }
          break;
        default:
          if ('others' in productsAppendingList){
            productsAppendingList.others.push(productSection);
          }
          else{
            productsAppendingList.others = [productSection]
          }
          break;
      }
    });

    const group_mapping = {
      genai:genai_group,
      cv:cv_group,
      others:others_grp
    }

    Object.keys(productsAppendingList).forEach((key)=>{
      const productsCollectionContainer = createElementFunction('div','productsCollectionContainer')
      productsAppendingList[key].forEach((productElement)=>{
        productsCollectionContainer.appendChild(productElement);
      })
      group_mapping[key].appendChild(productsCollectionContainer)
    })
    const collapse = document.querySelectorAll('.fa-angle-up');
    collapse.forEach((element, index) => {
      element.addEventListener('click', () => {
        element.parentElement.parentElement.classList.toggle('lessMarginBottom');
        element.parentElement.parentElement.nextElementSibling.classList.toggle('collapse');
        element.classList.toggle('activate');
      });
    });



  // Function to create the popup and overlay
  function createPopup(productIndex) {
    const popup = document.createElement('div');
    popup.className = 'popup-container';
    let popupBodyContent = ''
    if (products[productIndex].username){
      popupBodyContent = `<div class='credit-con'>
                                  <p>Email</p>
                                  <div class='credit-value'>
                                    <p id="Username">${products[productIndex].username}</p>
                                    <i class="fa-regular fa-copy" data-copy="Username"></i>
                                  </div>
                                </div>
                                <div class='credit-con'>
                                  <p>Password</p>
                                  <div class='credit-value'>
                                    <p id="Password">${products[productIndex].password}</p>
                                    <i class="fa-regular fa-copy" data-copy="Password"></i>
                                  </div>
                                </div>
                              </div>`
    }else{
      popupBodyContent = `<div class='no-credit-con credit-con' style=" padding:20px 0px">
                            <p id='warning' style=" width:100%;text-align:center">No Credientials Available</p>
                          </div>`
                        }


    popup.innerHTML = `
      <div id='popup-header'>
        <h1>Demo Credentials</h1>
        <i class="fa-solid fa-xmark" id='cancel-overlay'></i>
      </div>
      <div id='popup-body'>
          ${popupBodyContent}
      <div id='popup-footer'>
        <a href="${products[productIndex].link}" target="_blank">
          Visit Site <i class="fa-solid fa-arrow-up-right-from-square"></i>
        </a>
      </div>
    `;

    const html = document.querySelector('html');
    const overlay = document.createElement('div');
    overlay.className = 'overlay';
    html.appendChild(overlay);
    html.appendChild(popup);

    html.style.overflow = 'hidden';

    const cancelOverlay = document.querySelector('#cancel-overlay');
    cancelOverlay.addEventListener('click', () => {
      overlay.remove();
      popup.remove();
      html.style.overflow = '';
    });

    const copyButtons = document.querySelectorAll('.fa-copy');
    copyButtons.forEach((button) => {
      button.addEventListener('click', (event) => {
        let copyTarget = event.target.getAttribute('data-copy');
        const textToCopy = document.getElementById(copyTarget).innerText;
        navigator.clipboard.writeText(textToCopy).then(() => {
          alert(`${copyTarget} Copied To Clipboard`);
        });
      });
    });
  }

  const redirects = document.querySelectorAll('.redirect-btn');
  redirects.forEach((element) => {
    element.addEventListener('click', () => {
      createPopup(element.getAttribute('index'));
    });
  });

    
  });