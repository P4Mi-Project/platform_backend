from serializers import serializer
from configs.firebase_admin_config import db
from fastapi.exceptions import HTTPException
from services.EmailService import EmailService
from rapidfuzz import fuzz
import json

class CommunityPostService:
    '''
    this should give first 20 posts.
    page value will be the page number. 
    Search on internet about pagination if you don't know about pagination.
    '''
    # todo
    def get_posts(self,page:int, limit:int)->list[str]:
        try:
            return db.collections("community_posts").limit(limit).get()
        except:
            import traceback; traceback.print_exc()
            raise HTTPException(status_code=500, detail="Something went wrong while trying to fetch the post list from the database. Plesae have a look at the log.")
        

    def add_post(self, community_post:serializer.CommunityPost)-> serializer.ServerResponse:
        try:
            db.collection("community_posts").add(community_post.model_dump(mode = "json"))
        except:
            import traceback; traceback.print_exc()
            raise HTTPException(status_code=500, detail="Something went wrong while trying to add post to the database. Please have a look at the log.")
        
    def delete_post(self,post_id:str) -> serializer.ServerResponse:
        try:
            db.collection("community_posts").document(post_id).delete()
            return serializer.ServerResponse(status="200", message="The post has been deleted successfully.")
        except:
            import traceback; traceback.print_exc()
            raise HTTPException(status_code=500, detail="Something went wrong while trying to delete community post from database. Please have a look at the log.")
        
    def edit_post(self,post_id:str,community_post:serializer.CommunityPost) -> serializer.ServerResponse:
        try:
            result = db.collection("community_posts").document(post_id).get()
            if len(result) > 0:
                db.collection("community_posts").document(post_id).set(community_post.model_dump(mode = "json"),merged = True)
            
            return serializer.ServerResponse(status="200", message="Something went wrong while trying to edit the post. Please have a look at the log.")
        except:
            import traceback; traceback.print_exc()
            raise HTTPException(status_code=500, detail="Something went wrong while trying to edit the community post. Plesae have a look at the log.")
    
    def get_post_based_on_category(self, category:str) -> list[serializer.CommunityPost]:
        try:
            filtered_category_list = list()
            
            list_of_post = db.collection("community_posts").get()
            
            for post_item in list_of_post:
                if category in post_item.get("categories"):
                    filtered_category_list.append(post_item)
                    
            return filtered_category_list
        except:
            import traceback; traceback.print_exc()
            raise HTTPException(status_code=500, detail="Something went wrong while trying to get post by category. Please have a look at the log.")
    '''
    Post searching mechanism
    '''
    def get_post_by_text(self, search_text:str):
        try:
            filtered_post_list = list()
            
            converted_search_text = search_text.replace(" ", "")
            post_list = db.collection("community_posts").get()
            for post_item in post_list:
                # need to check both title and body
                # checking the title
                search_able_title = post_item.get("title").replace(" ","")
                search_able_body = post_item.get("body").replace(" ", "")
                
                if fuzz.ratio(converted_search_text,search_able_title) > 85:
                    filtered_post_list.append(post_item)
                elif fuzz.ratio(converted_search_text,search_able_body) > 85:
                    filtered_post_list.append(post_item)
                    
            return filtered_post_list
        except:
            import traceback; traceback.print_exc();
            raise HTTPException(status_code=500, detail = "Something went wrong while trying to get post by text. Plesae have a look at the log.")
        
    def hide_post(self,post_id:str)-> serializer.ServerResponse:
        try:
            result = db.collection("community_posts").document(post_id).get()
            if len(result) > 0:
                parsed_result = json.load(result[0])
                parsed_result["is_hidden"] = True
                db.collection("community_posts").document(post_id).set(parsed_result,merged = True)
        except:
            import traceback; traceback.print_exc()
            raise HTTPException(status_code=500, detail="Something went wrong while trying to hide post. Please have a look at the log.")
        
    def show_post(self, post_id:str) -> serializer.ServerResponse:
        try:
            result = db.collection("community_posts").document(post_id).get()
            if len(result) > 0:
                parsed_result = json.load(result[0])
                parsed_result["is_hidden"] = False
                db.collection("community_posts").document(post_id).set(parsed_result,merged = True)
        except:
            import traceback; traceback.print_exc()
            raise HTTPException(status_code=500, detail="Something went wrong while trying to show the post. Please have a look at the log.")