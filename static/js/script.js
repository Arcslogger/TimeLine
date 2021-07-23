var typed = new Typed(".typing", {
  strings: ["safer", "convenient", "easier"],
  typeSpeed: 100,
  backSpeed: 60,
  loop: true
});

function initMap() {
const input = document.getElementById("pac-input");
const options = {
  componentRestrictions: { country: "can" },
  fields: ["formatted_address", "geometry", "name"],
  strictBounds: false,
  types: [],
};
const autocomplete = new google.maps.places.Autocomplete(input, options);
autocomplete.addListener("place_changed", () => {
  const place = autocomplete.getPlace();
  if (!place.geometry || !place.geometry.location) {
    // User entered the name of a Place that was not suggested and
    // pressed the Enter key, or the Place Details request failed.
    window.alert("No details available for input: '" + place.name + "'");
    return;
  }
  
});
}

function loadJSON(){
  fetch('/static/js/data.json')
        .then(response => response.json())
        .then(data => {
            console.log(data)
            if (data.length==0){
              document.getElementById("wrapper").innerHTML = "";
              let wrap = document.querySelector('#wrapper');
              let div = document.createElement('div');
              div.className = 'mainDiv';
              let text = document.createTextNode('⚠️ Uh oh! ⚠️');
              div.append(text);
              div.appendChild(document.createElement("br"));
              div.append('No places were found or open!');
              wrap.appendChild(div);
            }
            else{
              document.getElementById("wrapper").innerHTML = "";
              let wrap = document.querySelector('#wrapper')
              for (i=0; i<data.length; i++){
                let div = document.createElement('div');
                div.className = 'mainDiv';
                
                let top = document.createElement('div');
                top.className = 'top'
                let middle = document.createElement('div');
                middle.className = 'middle'
                let bottomLeft = document.createElement('div');
                bottomLeft.className = 'bottomLeft'
                let bottomRight = document.createElement('div')
                bottomRight.className = 'bottomRight'

                let nameClass = document.createElement('div');
                nameClass.className = 'name';
                let placeName = document.createTextNode(data[i].name);

                let busyClass = document.createElement('div');
                busyClass.className = 'busy';
                let placeBusy = document.createTextNode(data[i].busyness + "% Busy");

                let ratingClass = document.createElement('div');
                ratingClass.className = 'rating';
                let placeRating = document.createTextNode(data[i].rating + "/5 ⭐");

                let addressClass = document.createElement('div');
                addressClass.className = 'address';
                let placeAddress = document.createTextNode(data[i].address);

                let clickLink = document.createElement('a'); 

                // Set the href property.
                let endURL = data[i].name + " " + data[i].address;
                console.log(endURL);
                clickLink.href = "https://www.google.com/search?q=" + endURL; 
                clickLink.target = "_blank";
                clickLink.append(placeName);
                nameClass.appendChild(clickLink);


                // nameClass.appendChild(placeName);
                busyClass.appendChild(placeBusy);
                ratingClass.appendChild(placeRating);
                addressClass.appendChild(placeAddress); 

                top.append(nameClass);
                middle.append(addressClass);
                bottomLeft.append(placeBusy);
                bottomRight.append(ratingClass)

                div.append(top);
                div.append(middle);
                div.append(bottomLeft);
                div.append(bottomRight);

                wrap.appendChild(div);
            }
            }
        })
}