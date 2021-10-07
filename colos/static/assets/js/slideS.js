

const slideshowText = document.querySelectorAll(".slideshow-text");


const nextTextDelay= 2000;
let counter1 = 0;


slideshowText[counter1].style.opacity = 1;


setInterval(nextText, nextTextDelay);


function nextText() {

	const temp1 = counter1;

	setTimeout(() => {
	slideshowText[temp1].style.opacity = 0;
	}, 2000);


counter1 = (counter1 + 1) % slideshowText.length;
slideshowText[counter1].style.opacity = 1;


}

