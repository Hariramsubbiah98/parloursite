var script = document.createElement('script');
script.src = 'https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js';

script.onload = function() {
    console.log('jQuery loaded!');

    // jQuery code can now safely execute
    $(document).ready(function() {
        $("#loadMore").on('click', function() {
            console.log('Button clicked!');
            // Add your logic here for what happens when the button is clicked
        });
    });
};

// Append the script element to the head of the document
document.head.appendChild(script);
