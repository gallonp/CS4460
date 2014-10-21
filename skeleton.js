<script>
// code to make coordindate for 

//line object to interpolate pixel values for course GPA lines
var line = d3.svg.line()
    .interpolate("basis")
    .x(function(d) { return x(d.year); })
    .y(function(d) { return y(d.gpa); });


/////////////////////////////////
/* csv file Reading example
year.csv:

year,age,sex,people
1850,0,1,1483789

d3.csv("population.csv",function(d){
  return{
    // the plus sign means tranforming the data into numeric data rather than string
    year: +d.year,
    age: +d.age,
    sex: +d.sex,
    people: +d.people,
  };
}, function(error, rows){
    // This is the callback funciton that will process the csv file once it is imported
    // rows is an iterator that stores all the rows in the csv file
 
    // A var to store all the different ages to be used in x-axis 
    var ages = d3.set();
    
    //extract all different years to be used to draw different lines
    var year_key = d3.set(rows.map(function(d){
          return d.year;
    }));
}

*/
/////////////////////////////////

// code to bind data into view
d3.csv("file to read",function(d){
  return{
    //'column name in csvfile':'object key in javascript'
    name: +d.value,
  }

  //

}, function(error, rows){











  //Code to be executed when selecting certain college
  //$(".college_menu").change(function(){
  //});

  //Code to be executed when selecting certain college
  //$(".college_menu").change(function(){
  //});
}


function draw_GPA_Lines(courses, svg, color){

// Draw lines representing the GPA trend for the courses in the past 4 years in svg
    var courses = svg.selectAll(".courses")
      .data(courses)
    .enter().append("g")
      .attr("class", "courses");
    //code to draw 
    courses.append("path")
      .attr("class", "line")
      .style("stroke", function(d) { return color(d.year); })
      .style("opacity","0")
      .transition()
        .duration(250)
        .delay(function(d,i){
          return (i%(years.length/2))*250
        })
        .attr("d", function(d) { return line(d.year); })        
        .style("opacity","0.5");


}

function draw_grade_distribution_pie_chart(course, svg, color){

}






</script>