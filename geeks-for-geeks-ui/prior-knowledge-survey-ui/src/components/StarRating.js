import React, {useState} from "react"
import {FaStar} from "react-icons/fa"
 const StarRating = () => {

     const [rating, setRating] = useState(null);
     const [hover, sethover] = useState(null)

     return (

         <div>
             {[...Array(5)].map((star, iterator) => {
                 const ratingValue = iterator + 1
                 return (
                     <label>
                         <input type="radio"
                                name="rating"
                                value={ratingValue}
                                onClick={() => setRating(ratingValue)}
                         />
                         <FaStar className="star"
                                 onMouseEnter={() => setRating(ratingValue)}
                                 onMouseLeave={() => setRating(null)}
                                 color={ratingValue <= (hover || rating) ? "#ffc107" : "#e4e5e9"} size={60}/>
                     </label>
                 );
             })}<p style={{fontSize:"60%"}}>{rating < 3 ? "Beginner" : (rating >=3 && rating <=4) ? "Intermediate" : rating > 4 ? "Advanced" : null}</p>

         </div>

     )
 }
export default StarRating;