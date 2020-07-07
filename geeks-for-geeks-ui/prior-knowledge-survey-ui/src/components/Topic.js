import React from "react"
import StarRating from "./StarRating";
import {Link} from "react-router-dom";


class Topic extends React.Component {

    constructor() {
        super()
        this.state={
            loading:false,
            topic:{}
        }
    }

    componentDidMount() {
    this.setState({loading:true})
    fetch("http://localhost:5000/topics")
        .then(response => response.json())
        .then(data => this.setState({topic: data, loading:false}))
  }


    render() {
        /*
        This needs to be changed with a map function
         */
        let datatest={"1": "SQL", "2": "Python", "3": "Spark", "4": "Cloud Computing", "5": "Machine Learning", "6": "Probability", "7": "Statistics"}
        const topic= Object.values(datatest)
        let ratings=topic.map(subject =><div className="rating">
            <div className="subject" style={{display:"inline-block",justifyContent:"center",alignItems:"center",verticalAlign:"middle",color:"#02075d"}}><b>{subject}</b></div>
            <div className="star-rating" style={{display:"inline-block",float:"right" }}>
            <StarRating/></div>
        </div>)
        //const topic= topicsData.map(item => item)
        return(
         <div>
             <p style={{textAlign:"center", color:"#02075d"}} ><b>Rate your knowledge to help us customize your learning experience</b></p>

             <h4>{ratings}</h4>
             <Link to="/thank_you">
                  <div className="wrapper" style={{textAlign: "center"}}>
                <button className="btn btn-success" style={{position: "center"}}>Submit</button>
            </div>
             </Link>
         </div>
        )
    }


}

export default Topic;