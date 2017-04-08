from flask import Flask, jsonify
app = Flask(__name__)

from raspberrypy.sensor.GY521 import GY521
gy = GY521()

@app.route('/update', methods=['POST'])
def update():
  res = gy.get_all_data()
  return jsonify(temp=res['temp'], 
                  acc_x=res['accel'].x,
                  acc_y=res['accel'].y,
                  acc_z=res['accel'].z,
                  gyro_x=res['gyro'].x,
                  gyro_y=res['gyro'].y,
                  gyro_z=res['gyro'].z)

@app.route('/')
def index():
  return '''
<!DOCTYPE HTML>
<html>
  <head>
     <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/canvasjs/1.7.0/canvasjs.min.js"></script>
    <script>
    $( document ).ready(function() {
      var temp = []; // temperature 
      var acc_x = []; 
      var acc_y = []; 
      var acc_z = []; 
      var gyro_x = [];
      var gyro_y = [];
      var gyro_z = [];

      var chart = new CanvasJS.Chart("chartContainer",{
                    title :{ text: "motor monitor" },      
                    data:  [{ type: "line",
                              showInLegend: true, 
                              legendText: "temperature",
                              dataPoints: temp},
                            { type: "line",
                              showInLegend: true, 
                              legendText: "acceleration_x",
                              dataPoints: acc_x},
                            { type: "line",
                              showInLegend: true, 
                              legendText: "acceleration_y",
                              dataPoints: acc_y},
                             { type: "line",
                              showInLegend: true, 
                              legendText: "acceleration_z",
                              dataPoints: acc_z},
                            { type: "line",
                              showInLegend: true, 
                              legendText: "gyroscope_x",
                              dataPoints: gyro_x},
                            { type: "line",
                              showInLegend: true, 
                              legendText: "gyroscope_y",
                              dataPoints: gyro_y},
                            { type: "line",
                              showInLegend: true, 
                              legendText: "gyroscope_z",
                              dataPoints: gyro_z}],

                            legend: {
                              cursor: "pointer",
                                    itemclick: function (e) {
                                      //console.log("legend click: " + e.dataPointIndex);
                                      //console.log(e);
                                      if (typeof (e.dataSeries.visible) === "undefined" || e.dataSeries.visible) {
                                        e.dataSeries.visible = false;
                                      } else {
                                        e.dataSeries.visible = true;
                                      }
                                      e.chart.render();
                              }
                            },
                  });

      var updateInterval = 100;
      var dataLength = 50;
      var t = 0;

      var updateChart = function () {
        t++;
        $.ajax({
            url: '/update',
            type: 'POST',
            success: function(res) {
//               console.log(res);
               temp.push({x:t, y:res.temp});
               acc_x.push({x:t, y:res.acc_x});
               acc_y.push({x:t, y:res.acc_y});
               acc_z.push({x:t, y:res.acc_z});
               gyro_x.push({x:t, y:res.gyro_x});
               gyro_y.push({x:t, y:res.gyro_y});
               gyro_z.push({x:t, y:res.gyro_z});
            },
            error: function() { console.log("Error"); }
          });
        if (temp.length > dataLength) {
          temp.shift();        
          acc_x.shift();
          acc_y.shift();
          acc_z.shift();
          gyro_x.shift();
          gyro_y.shift();
          gyro_z.shift();
        }
        chart.render();   
      }; 

      setInterval(function(){updateChart()}, updateInterval); 
    });
    </script>
  </head>

  <body>
    <div id="chartContainer" style="height: 300px; width:100%;">
    </div>
  </body>
</html>
'''

if __name__ == '__main__':
  app.run(host='0.0.0.0')
