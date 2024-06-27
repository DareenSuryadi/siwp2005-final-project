from flask import request, jsonify, abort, Response
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import current_app as app
from marshmallow.exceptions import ValidationError
from mongoengine.errors import NotUniqueError
from werkzeug.exceptions import UnprocessableEntity, Conflict

import helper.validator as validator
from model.course import Course, User, Bulletin, Billing, Academic, Softskill
from helper.schema import CourseSchema, BulletinSchema, BillingSchema, AcademicSchema, SoftskillSchema

class CourseListAPI(Resource):
    @jwt_required()
    def get(self):
        courses = Course.objects()
        serialized_payload = CourseSchema(many=True).dump(courses)
        return serialized_payload, 200
    
    @jwt_required()
    def post(self):
        serialized_payload = validator.add_course()
        course = Course(**serialized_payload)
        course.save()
        serialized_payload = CourseSchema().dump(course)
        return serialized_payload, 200

class CourseAPI(Resource):
    @jwt_required()
    def get(self, course_id):
        course = Course.objects.get(id=course_id)
        serialized_payload = CourseSchema().dump(course)
        return serialized_payload, 200
    
    @jwt_required()
    def put(self, course_id):
        course = Course.objects.get(id=course_id)
        user = User.objects.get(id=get_jwt_identity())
        serialized_payload = validator.add_course()
        for key, value in serialized_payload.items():
            setattr(course, key, value)
        course.save()
        serialized_payload = CourseSchema().dump(course)
        return serialized_payload, 200
    
    @jwt_required()
    def delete(self, course_id):        
        course = Course.objects.get(id=course_id)
        course.delete()
        app.logger.info("Course with id %s deleted", course_id)
        msg={"message": "Course: {} deleted".format(course_id)}
        return msg, 200
    
class BulletinListAPI(Resource):
    @jwt_required()
    def get(self):
        bulletin = Bulletin.objects()
        serialized_payload = BulletinSchema(many=True).dump(bulletin)
        return serialized_payload, 200
    
    @jwt_required()
    def post(self):
        serialized_payload = validator.add_bulletin()
        bulletin = Bulletin(**serialized_payload)
        bulletin.save()
        serialized_payload = BulletinSchema().dump(bulletin)
        return serialized_payload, 200

class BulletinAPI(Resource):
    @jwt_required()
    def get(self, bulletin_id):
        app.logger.info("bulletin id: {}".format(bulletin_id))
        bulletin = Bulletin.objects.get(id=bulletin_id)
        serialized_payload = BulletinSchema().dump(bulletin)
        return serialized_payload, 200
    
    @jwt_required()
    def put(self, bulletin_id):
        bulletin = Bulletin.objects.get(id=bulletin_id)
        user = User.objects.get(id=get_jwt_identity())
        serialized_payload = validator.add_bulletin()
        for key, value in serialized_payload.items():
            setattr(bulletin, key, value)
        bulletin.save()
        serialized_payload = BulletinSchema().dump(bulletin)
        return serialized_payload, 200
    
    @jwt_required()
    def delete(self, bulletin_id):        
        bulletin = Bulletin.objects.get(id=bulletin_id)
        bulletin.delete()
        app.logger.info("Bulletin with id %s deleted", bulletin_id)
        msg={"message": "Bulletin: {} deleted".format(bulletin_id)}
        return msg, 200
    
class BillingListAPI(Resource):
    @jwt_required()
    def get(self):
        billing = Billing.objects()
        serialized_payload = BillingSchema(many=True).dump(billing)
        return serialized_payload, 200
    
    @jwt_required()
    def post(self):
        serialized_payload = validator.add_billing()
        billing = Billing(**serialized_payload)
        billing.save()
        serialized_payload = BillingSchema().dump(billing)
        return serialized_payload, 200

class BillingAPI(Resource):
    @jwt_required()
    def get(self, billing_id):
        app.logger.info("billing id: {}".format(billing_id))
        billing = Billing.objects.get(id=billing_id)
        serialized_payload = BillingSchema().dump(billing)
        return serialized_payload, 200
    
    @jwt_required()
    def put(self, billing_id):
        billing = Billing.objects.get(id=billing_id)
        user = User.objects.get(id=get_jwt_identity())
        serialized_payload = validator.add_billing()
        for key, value in serialized_payload.items():
            setattr(billing, key, value)
        billing.save()
        serialized_payload = BillingSchema().dump(billing)
        return serialized_payload, 200
    
    @jwt_required()
    def delete(self, billing_id):        
        billing = Billing.objects.get(id=billing_id)
        billing.delete()
        app.logger.info("Billing with id %s deleted", billing_id)
        msg={"message": "Billing: {} deleted".format(billing_id)}
        return msg, 200
    
class AcademicListAPI(Resource):
    @jwt_required()
    def get(self):
        academic = Academic.objects()
        serialized_payload = AcademicSchema(many=True).dump(academic)
        return serialized_payload, 200
    
    @jwt_required()
    def post(self):
        serialized_payload = validator.add_academic()
        academic = Academic(**serialized_payload)
        academic.save()
        serialized_payload = AcademicSchema().dump(academic)
        return serialized_payload, 200

class AcademicAPI(Resource):
    @jwt_required()
    def get(self, academic_id):
        app.logger.info("academic id: {}".format(academic_id))
        academic = Academic.objects.get(id=academic_id)
        serialized_payload = AcademicSchema().dump(academic)
        return serialized_payload, 200
    
    @jwt_required()
    def put(self, academic_id):
        academic = Academic.objects.get(id=academic_id)
        user = User.objects.get(id=get_jwt_identity())
        serialized_payload = validator.add_academic()
        for key, value in serialized_payload.items():
            setattr(academic, key, value)
        academic.save()
        serialized_payload = AcademicSchema().dump(academic)
        return serialized_payload, 200
    
    @jwt_required()
    def delete(self, academic_id):        
        academic = Academic.objects.get(id=academic_id)
        academic.delete()
        app.logger.info("Academic with id %s deleted", academic_id)
        msg={"message": "Academic: {} deleted".format(academic_id)}
        return msg, 200

class SoftskillListAPI(Resource):
    @jwt_required()
    def get(self):
        softskill = Softskill.objects()
        serialized_payload = SoftskillSchema(many=True).dump(softskill)
        return serialized_payload, 200
    
    @jwt_required()
    def post(self):
        serialized_payload = validator.add_softskill()
        softskill = Softskill(**serialized_payload)
        softskill.save()
        serialized_payload = SoftskillSchema().dump(softskill)
        return serialized_payload, 200

class SoftskillAPI(Resource):
    @jwt_required()
    def get(self, softskill_id):
        app.logger.info("softskill id: {}".format(softskill_id))
        softskill = Softskill.objects.get(id=softskill_id)
        serialized_payload = SoftskillSchema().dump(softskill)
        return serialized_payload, 200
    
    @jwt_required()
    def put(self, softskill_id):
        softskill = Softskill.objects.get(id=softskill_id)
        user = User.objects.get(id=get_jwt_identity())
        serialized_payload = validator.add_softskill()
        for key, value in serialized_payload.items():
            setattr(softskill, key, value)
        softskill.save()
        serialized_payload = SoftskillSchema().dump(softskill)
        return serialized_payload, 200
    
    @jwt_required()
    def delete(self, softskill_id):        
        softskill = Softskill.objects.get(id=softskill_id)
        softskill.delete()
        app.logger.info("Softskill with id %s deleted", softskill_id)
        msg={"message": "Softskill: {} deleted".format(softskill_id)}
        return msg, 200