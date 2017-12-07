// jQuery(function( $ ){
//     $('.close-alert').click(function( e ){
//         e.preventDefault();
//         $.cookie('alert', 'closed', { path: '/' });
//     });
// });

// jQuery(function( $ ){
//     if( $.cookie('alert') === 'closed' ){
//         $('.alert').hide();
//     }
// });

function saveactivity(name){
	console.log("Submitting: "+name)
	data = JSON.stringify({"name":name});
	$.post( "/saveactivity", data, function( data ) {
	  console.log( data );
	});
}